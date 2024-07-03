def validateIP(ip):
  """
  @param ip: str
  @return: bool
  """
  nums = ip.split('.')

  if len(nums) != 4:
    return False


  for num in nums:

    if not num.isdigit():
      return False

    aNum = int(num)

    if aNum < 0 or aNum > 255:
      return False
  return True

# debug your code below
print(validateIP('192.168.0.1'))
