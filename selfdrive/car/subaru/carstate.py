import copy
from cereal import car
from opendbc.can.can_define import CANDefine
from selfdrive.config import Conversions as CV
from selfdrive.car.interfaces import CarStateBase
from opendbc.can.parser import CANParser
from selfdrive.car.subaru.values import DBC, STEER_THRESHOLD, CAR, PREGLOBAL_CARS
from common.params import Params


class CarState(CarStateBase):
  def __init__(self, CP):
    super().__init__(CP)
    can_define = CANDefine(DBC[CP.carFingerprint]["pt"])
    self.shifter_values = can_define.dv["Transmission"]["Gear"]

    params = Params()
    self.has_epb = params.get("ManualParkingBrakeSNGToggle", encoding='utf8') == "0"

  def update(self, cp, cp_cam, cp_body):
    ret = car.CarState.new_message()

    if self.car_fingerprint == CAR.CROSSTREK_2020H:
      ret.gas = cp_body.vl["Throttle_Hybrid"]["Throttle_Pedal"] / 255.
    else:
      ret.gas = cp.vl["Throttle"]["Throttle_Pedal"] / 255.
    ret.gasPressed = ret.gas > 1e-5
    if self.car_fingerprint in PREGLOBAL_CARS:
      ret.brakePressed = cp.vl["Brake_Pedal"]["Brake_Pedal"] > 2
    elif self.car_fingerprint == CAR.OUTBACK:
      ret.brakePressed = cp_body.vl["Brake_Status"]["Brake"] == 1
    elif self.car_fingerprint == CAR.CROSSTREK_2020H:
      ret.brakePressed = cp_body.vl["Brake_Hybrid"]["Brake"] == 1
    else:
      ret.brakePressed = cp.vl["Brake_Status"]["Brake"] == 1

    if self.car_fingerprint == CAR.OUTBACK:
      ret.wheelSpeeds.fl = cp_body.vl["Wheel_Speeds"]["FL"] * CV.KPH_TO_MS
      ret.wheelSpeeds.fr = cp_body.vl["Wheel_Speeds"]["FR"] * CV.KPH_TO_MS
      ret.wheelSpeeds.rl = cp_body.vl["Wheel_Speeds"]["RL"] * CV.KPH_TO_MS
      ret.wheelSpeeds.rr = cp_body.vl["Wheel_Speeds"]["RR"] * CV.KPH_TO_MS
    else:
      ret.wheelSpeeds.fl = cp.vl["Wheel_Speeds"]["FL"] * CV.KPH_TO_MS
      ret.wheelSpeeds.fr = cp.vl["Wheel_Speeds"]["FR"] * CV.KPH_TO_MS
      ret.wheelSpeeds.rl = cp.vl["Wheel_Speeds"]["RL"] * CV.KPH_TO_MS
      ret.wheelSpeeds.rr = cp.vl["Wheel_Speeds"]["RR"] * CV.KPH_TO_MS
    ret.vEgoRaw = (ret.wheelSpeeds.fl + ret.wheelSpeeds.fr + ret.wheelSpeeds.rl + ret.wheelSpeeds.rr) / 4.
    # Kalman filter, even though Subaru raw wheel speed is heaviliy filtered by default
    ret.vEgo, ret.aEgo = self.update_speed_kf(ret.vEgoRaw)
    ret.standstill = ret.vEgoRaw < 0.01

    # continuous blinker signals for assisted lane change
    ret.leftBlinker, ret.rightBlinker = self.update_blinker_from_lamp(
      50, cp.vl["Dashlights"]["LEFT_BLINKER"], cp.vl["Dashlights"]["RIGHT_BLINKER"])

    if self.CP.enableBsm:
      ret.leftBlindspot = (cp.vl["BSD_RCTA"]["L_ADJACENT"] == 1) or (cp.vl["BSD_RCTA"]["L_APPROACHING"] == 1)
      ret.rightBlindspot = (cp.vl["BSD_RCTA"]["R_ADJACENT"] == 1) or (cp.vl["BSD_RCTA"]["R_APPROACHING"] == 1)

    if self.car_fingerprint == CAR.CROSSTREK_2020H:
      can_gear = int(cp_body.vl["Transmission"]["Gear"])
    else:
      can_gear = int(cp.vl["Transmission"]["Gear"])
    ret.gearShifter = self.parse_gear_shifter(self.shifter_values.get(can_gear, None))

    if self.car_fingerprint == CAR.WRX_PREGLOBAL:
      ret.steeringAngleDeg = cp.vl["Steering"]["Steering_Angle"]
    else:
      ret.steeringAngleDeg = cp.vl["Steering_Torque"]["Steering_Angle"]
    ret.steeringTorque = cp.vl["Steering_Torque"]["Steer_Torque_Sensor"]
    ret.steeringPressed = abs(ret.steeringTorque) > STEER_THRESHOLD[self.car_fingerprint]

    if self.car_fingerprint == CAR.OUTBACK:
      ret.cruiseState.enabled = cp_body.vl["CruiseControl"]["Cruise_Activated"] != 0
      ret.cruiseState.available = cp_body.vl["CruiseControl"]["Cruise_On"] != 0
    elif self.car_fingerprint == CAR.CROSSTREK_2020H:
      ret.cruiseState.enabled = cp_cam.vl["ES_DashStatus"]['Cruise_Activated'] != 0
      ret.cruiseState.available = cp_cam.vl["ES_DashStatus"]['Cruise_On'] != 0
    else:
      ret.cruiseState.enabled = cp.vl["CruiseControl"]["Cruise_Activated"] != 0
      ret.cruiseState.available = cp.vl["CruiseControl"]["Cruise_On"] != 0
    ret.cruiseState.speed = cp_cam.vl["ES_DashStatus"]["Cruise_Set_Speed"] * CV.KPH_TO_MS

    if self.car_fingerprint not in PREGLOBAL_CARS and cp.vl["Dashlights"]["UNITS"] == 1:
      ret.cruiseState.speed *= CV.MPH_TO_KPH
    elif self.car_fingerprint in PREGLOBAL_CARS and cp.vl["Dash_State2"]["Units"] == 1:
      ret.cruiseState.speed *= CV.MPH_TO_KPH

    ret.seatbeltUnlatched = cp.vl["Dashlights"]["SEATBELT_FL"] == 1
    ret.doorOpen = any([cp.vl["BodyInfo"]["DOOR_OPEN_RR"],
                        cp.vl["BodyInfo"]["DOOR_OPEN_RL"],
                        cp.vl["BodyInfo"]["DOOR_OPEN_FR"],
                        cp.vl["BodyInfo"]["DOOR_OPEN_FL"]])
    ret.steerError = cp.vl["Steering_Torque"]["Steer_Error_1"] == 1
    self.throttle_msg = copy.copy(cp.vl["Throttle"])

    if self.car_fingerprint in PREGLOBAL_CARS:
      self.cruise_button = cp_cam.vl["ES_Distance"]["Cruise_Button"]
      self.ready = not cp_cam.vl["ES_DashStatus"]["Not_Ready_Startup"]
      self.es_distance_msg = copy.copy(cp_cam.vl["ES_Distance"])
      self.car_follow = cp_cam.vl["ES_Distance"]["Car_Follow"]
      self.close_distance = cp_cam.vl["ES_Distance"]["Close_Distance"]
    else:
      ret.steerWarning = cp.vl["Steering_Torque"]["Steer_Warning"] == 1
      ret.cruiseState.nonAdaptive = cp_cam.vl["ES_DashStatus"]["Conventional_Cruise"] == 1
      self.cruise_state = cp_cam.vl["ES_DashStatus"]["Cruise_State"]
      self.brake_pedal_msg = copy.copy(cp.vl["Brake_Pedal"])
      self.es_lkas_msg = copy.copy(cp_cam.vl["ES_LKAS_State"])
      if self.car_fingerprint == CAR.OUTBACK:
        self.car_follow = cp_body.vl["ES_Distance"]["Car_Follow"]
        self.close_distance = cp_body.vl["ES_Distance"]["Close_Distance"]
      # FIXME: find ES_Distance signals for CROSSTREK_2020H
      elif self.car_fingerprint != CAR.CROSSTREK_2020H:
        self.car_follow = cp_cam.vl["ES_Distance"]["Car_Follow"]
        self.close_distance = cp_cam.vl["ES_Distance"]["Close_Distance"]
        self.es_distance_msg = copy.copy(cp_cam.vl["ES_Distance"])
      self.es_dashstatus_msg = copy.copy(cp_cam.vl["ES_DashStatus"])

    return ret

  @staticmethod
  def get_can_parser(CP):
    # this function generates lists for signal, messages and initial values
    signals = [
      # sig_name, sig_address, default
      ("Steer_Torque_Sensor", "Steering_Torque", 0),
      ("Steering_Angle", "Steering_Torque", 0),
      ("Steer_Error_1", "Steering_Torque", 0),
      ("Brake_Pedal", "Brake_Pedal", 0),
      ("LEFT_BLINKER", "Dashlights", 0),
      ("RIGHT_BLINKER", "Dashlights", 0),
      ("SEATBELT_FL", "Dashlights", 0),
      ("DOOR_OPEN_FR", "BodyInfo", 1),
      ("DOOR_OPEN_FL", "BodyInfo", 1),
      ("DOOR_OPEN_RR", "BodyInfo", 1),
      ("DOOR_OPEN_RL", "BodyInfo", 1),
    ]
    checks = [
      # sig_address, frequency
      ("Throttle", 100),
      ("Brake_Pedal", 50),
      ("Steering_Torque", 50),
    ]

    # Wheel_Speeds is on can1 for OUTBACK
    if CP.carFingerprint != CAR.OUTBACK:
      signals += [
        ("FL", "Wheel_Speeds", 0),
        ("FR", "Wheel_Speeds", 0),
        ("RL", "Wheel_Speeds", 0),
        ("RR", "Wheel_Speeds", 0),
      ]
      checks += [
        ("Wheel_Speeds", 50),
      ]

    # Transmission is on can1 for CROSSTREK_2020H
    if CP.carFingerprint != CAR.CROSSTREK_2020H:
      signals += [
        ("Gear", "Transmission", 0),
      ]

      checks += [
        ("Transmission", 100),
      ]

    # CruiseControl is on can1 for OUTBACK and not used for CROSSTREK_2020H
    if CP.carFingerprint not in [CAR.OUTBACK, CAR.CROSSTREK_2020H]:
      signals += [
        ("Cruise_On", "CruiseControl", 0),
        ("Cruise_Activated", "CruiseControl", 0),
      ]

    if CP.carFingerprint in PREGLOBAL_CARS:
      signals += [
        ("Throttle_Pedal", "Throttle", 0),
        ("Counter", "Throttle", 0),
        ("Signal1", "Throttle", 0),
        ("Not_Full_Throttle", "Throttle", 0),
        ("Signal2", "Throttle", 0),
        ("Engine_RPM", "Throttle", 0),
        ("Off_Throttle", "Throttle", 0),
        ("Signal3", "Throttle", 0),
        ("Throttle_Cruise", "Throttle", 0),
        ("Throttle_Combo", "Throttle", 0),
        ("Throttle_Body", "Throttle", 0),
        ("Off_Throttle_2", "Throttle", 0),
        ("Signal4", "Throttle", 0),

        ("Units", "Dash_State2", 0),
        ("Steering_Angle", "Steering", 0),
      ]

      checks += [
        ("BodyInfo", 1),
        ("CruiseControl", 50),
        ("Dash_State2", 1),
        ("Steering", 50),
      ]

      if CP.carFingerprint in [CAR.FORESTER_PREGLOBAL, CAR.LEVORG_PREGLOBAL, CAR.WRX_PREGLOBAL]:
        checks += [
          ("Dashlights", 20),
        ]
      elif CP.carFingerprint in [CAR.LEGACY_PREGLOBAL, CAR.OUTBACK_PREGLOBAL, CAR.OUTBACK_PREGLOBAL_2018]:
        checks += [
          ("Dashlights", 10),
        ]

    else:
      signals += [
        ("Counter", "Throttle", 0),
        ("Signal1", "Throttle", 0),
        ("Engine_RPM", "Throttle", 0),
        ("Signal2", "Throttle", 0),
        ("Throttle_Pedal", "Throttle", 0),
        ("Throttle_Cruise", "Throttle", 0),
        ("Throttle_Combo", "Throttle", 0),
        ("Signal1", "Throttle", 0),
        ("Off_Accel", "Throttle", 0),

        ("Counter", "Brake_Pedal", 0),
        ("Signal1", "Brake_Pedal", 0),
        ("Speed", "Brake_Pedal", 0),
        ("Signal2", "Brake_Pedal", 0),
        ("Brake_Lights", "Brake_Pedal", 0),
        ("Signal3", "Brake_Pedal", 0),
        ("Signal4", "Brake_Pedal", 0),

        ("Steer_Warning", "Steering_Torque", 0),
        ("UNITS", "Dashlights", 0),
      ]

      checks += [
        ("Dashlights", 10),
        ("BodyInfo", 10),
      ]

      # Brake_Status is on can1 for OUTBACK
      if CP.carFingerprint != CAR.OUTBACK:
        signals += [
          ("Brake", "Brake_Status", 0),
        ]

        checks += [
          ("Brake_Status", 50),
        ]

      # CruiseControl is on can1 for OUTBACK and nod used for CROSSTREK_2020H
      if CP.carFingerprint not in [CAR.OUTBACK, CAR.CROSSTREK_2020H]:
        checks += [
          ("CruiseControl", 20),
        ]

    if CP.enableBsm:
      signals += [
        ("L_ADJACENT", "BSD_RCTA", 0),
        ("R_ADJACENT", "BSD_RCTA", 0),
        ("L_APPROACHING", "BSD_RCTA", 0),
        ("R_APPROACHING", "BSD_RCTA", 0),
      ]
      checks += [
        ("BSD_RCTA", 17),
      ]

    return CANParser(DBC[CP.carFingerprint]["pt"], signals, checks, 0)

  @staticmethod
  def get_body_can_parser(CP):
    signals = []
    checks = []

    if CP.carFingerprint == CAR.CROSSTREK_2020H:
      signals += [
        ("Throttle_Pedal", "Throttle_Hybrid", 0),
        ("Brake", "Brake_Hybrid", 0),
        ("Gear", "Transmission", 0),
      ]

      checks += [
        # sig_address, frequency
        ("Throttle_Hybrid", 50),
        ("Brake_Hybrid", 40),
        ("Transmission", 50),
      ]

      return CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, 1)

    elif CP.carFingerprint == CAR.OUTBACK:
      signals += [
        ("Cruise_On", "CruiseControl", 0),
        ("Cruise_Activated", "CruiseControl", 0),
        ("FL", "Wheel_Speeds", 0),
        ("FR", "Wheel_Speeds", 0),
        ("RL", "Wheel_Speeds", 0),
        ("RR", "Wheel_Speeds", 0),
        ("Brake", "Brake_Status", 0),
        ("Car_Follow", "ES_Distance", 0),
        ("Close_Distance", "ES_Distance", 0),
      ]

      checks += [
        ("CruiseControl", 20),
        ("ES_Distance", 20),
        ("Wheel_Speeds", 50),
        ("Brake_Status", 50),
      ]

      return CANParser(DBC[CP.carFingerprint]["pt"], signals, checks, 1)

    else:
      return None

  @staticmethod
  def get_cam_can_parser(CP):
    if CP.carFingerprint in PREGLOBAL_CARS:
      signals = [
        ("Cruise_Set_Speed", "ES_DashStatus", 0),
        ("Not_Ready_Startup", "ES_DashStatus", 0),
        ("Car_Follow", "ES_DashStatus", 0),

        ("Cruise_Throttle", "ES_Distance", 0),
        ("Signal1", "ES_Distance", 0),
        ("Car_Follow", "ES_Distance", 0),
        ("Signal2", "ES_Distance", 0),
        ("Brake_On", "ES_Distance", 0),
        ("Distance_Swap", "ES_Distance", 0),
        ("Standstill", "ES_Distance", 0),
        ("Signal3", "ES_Distance", 0),
        ("Close_Distance", "ES_Distance", 0),
        ("Signal4", "ES_Distance", 0),
        ("Standstill_2", "ES_Distance", 0),
        ("Cruise_Fault", "ES_Distance", 0),
        ("Signal5", "ES_Distance", 0),
        ("Counter", "ES_Distance", 0),
        ("Signal6", "ES_Distance", 0),
        ("Cruise_Button", "ES_Distance", 0),
        ("Signal7", "ES_Distance", 0),
      ]

      checks = [
        ("ES_DashStatus", 20),
        ("ES_Distance", 20),
      ]
    else:
      signals = [
        ("Counter", "ES_DashStatus", 0),
        ("PCB_Off", "ES_DashStatus", 0),
        ("LDW_Off", "ES_DashStatus", 0),
        ("Signal1", "ES_DashStatus", 0),
        ("Cruise_State_Msg", "ES_DashStatus", 0),
        ("LKAS_State_Msg", "ES_DashStatus", 0),
        ("Signal2", "ES_DashStatus", 0),
        ("Cruise_Soft_Disable", "ES_DashStatus", 0),
        ("EyeSight_Status_Msg", "ES_DashStatus", 0),
        ("Signal3", "ES_DashStatus", 0),
        ("Cruise_Distance", "ES_DashStatus", 0),
        ("Signal4", "ES_DashStatus", 0),
        ("Conventional_Cruise", "ES_DashStatus", 0),
        ("Signal5", "ES_DashStatus", 0),
        ("Cruise_Disengaged", "ES_DashStatus", 0),
        ("Cruise_Activated", "ES_DashStatus", 0),
        ("Signal6", "ES_DashStatus", 0),
        ("Cruise_Set_Speed", "ES_DashStatus", 0),
        ("Cruise_Fault", "ES_DashStatus", 0),
        ("Cruise_On", "ES_DashStatus", 0),
        ("Display_Own_Car", "ES_DashStatus", 0),
        ("Brake_Lights", "ES_DashStatus", 0),
        ("Car_Follow", "ES_DashStatus", 0),
        ("Signal7", "ES_DashStatus", 0),
        ("Far_Distance", "ES_DashStatus", 0),
        ("Cruise_State", "ES_DashStatus", 0),

        ("Counter", "ES_LKAS_State", 0),
        ("LKAS_Alert_Msg", "ES_LKAS_State", 0),
        ("Signal1", "ES_LKAS_State", 0),
        ("LKAS_ACTIVE", "ES_LKAS_State", 0),
        ("LKAS_Dash_State", "ES_LKAS_State", 0),
        ("Signal2", "ES_LKAS_State", 0),
        ("Backward_Speed_Limit_Menu", "ES_LKAS_State", 0),
        ("LKAS_Left_Line_Enable", "ES_LKAS_State", 0),
        ("LKAS_Left_Line_Light_Blink", "ES_LKAS_State", 0),
        ("LKAS_Right_Line_Enable", "ES_LKAS_State", 0),
        ("LKAS_Right_Line_Light_Blink", "ES_LKAS_State", 0),
        ("LKAS_Left_Line_Visible", "ES_LKAS_State", 0),
        ("LKAS_Right_Line_Visible", "ES_LKAS_State", 0),
        ("LKAS_Alert", "ES_LKAS_State", 0),
        ("Signal3", "ES_LKAS_State", 0),
      ]

      checks = [
        ("ES_DashStatus", 10),
        ("ES_LKAS_State", 10),
      ]

      if CP.carFingerprint not in [CAR.CROSSTREK_2020H, CAR.OUTBACK]:
        signals += [
          ("Counter", "ES_Distance", 0),
          ("Signal1", "ES_Distance", 0),
          ("Cruise_Fault", "ES_Distance", 0),
          ("Cruise_Throttle", "ES_Distance", 0),
          ("Signal2", "ES_Distance", 0),
          ("Car_Follow", "ES_Distance", 0),
          ("Signal3", "ES_Distance", 0),
          ("Cruise_Brake_Active", "ES_Distance", 0),
          ("Distance_Swap", "ES_Distance", 0),
          ("Cruise_EPB", "ES_Distance", 0),
          ("Signal4", "ES_Distance", 0),
          ("Close_Distance", "ES_Distance", 0),
          ("Signal5", "ES_Distance", 0),
          ("Cruise_Cancel", "ES_Distance", 0),
          ("Cruise_Set", "ES_Distance", 0),
          ("Cruise_Resume", "ES_Distance", 0),
          ("Signal6", "ES_Distance", 0),
        ]

        checks += [
          ("ES_Distance", 20),
        ]

    return CANParser(DBC[CP.carFingerprint]["pt"], signals, checks, 2)
