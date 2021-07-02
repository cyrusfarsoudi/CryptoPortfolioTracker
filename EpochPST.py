import time

class EpochPST:
  PST_EPOCH_OFFSET = 25200
  HOUR_SECONDS = 3600
  DAY_SECONDS = 86400
  WEEK_SECONDS = 604800
  MONTH_SECONDS = 2629743
  YEAR_SECONDS = 31556926

  def getPST():
    return time.time() - EpochPST.PST_EPOCH_OFFSET

  def getHourAgo():
    return EpochPST.getPST() - EpochPST.HOUR_SECONDS

  def getDayAgo():
    return EpochPST.getPST() - EpochPST.DAY_SECONDS

  def getWeekAgo():
    return EpochPST.getPST() - EpochPST.WEEK_SECONDS

  def getMonthAgo():
    return EpochPST.getPST() - EpochPST.MONTH_SEDONDS

  def getYearAgo():
    return EpochPST.getPST() - EpochPST.YEAR_SECONDS