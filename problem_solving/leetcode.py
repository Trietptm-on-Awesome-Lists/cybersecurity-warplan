# Anagram problem (Easy)
def anagram(A,B)
  """
  Returns an array which maps array A to array B
  Time complexity : O(N) + O(N) = O(N)
  Space complexity: O(N) since we are creating a
                      new hash map
  :type A: List[int]
  :type B: List[int]
  :rtype: List[int]
  """
  hash_b = {b:k for k,b in enumerate(B)}
  response = [hash_b[a] for a in A]
  return response


# Two Sum O(N)
def twoSumFaster(nums, target):
  """
  O(N) for hash
  O(1) for each search so O(N) complement searches
  O(N) for the loop.
  so O(2N) which means O(N)
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  my_hash = {}
  for a in range(0,len(nums)):
      my_hash[nums[a]] = a

  for indice_a in range(0,len(nums) - 1):
      diff = target - nums[indice_a]
      if diff in my_hash:
          for indice_b in range(indice_a + 1, len(nums)):
              if nums[indice_b] == diff:
                  return [indice_a, indice_b]

                
# 17-1-18
def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    move_dic = {"L":0,"R":0,"U":0,"D":0}
    complements = {"L":"R","U":"D"}
    for each_move in moves:
        move_dic[each_move] = move_dic[each_move] + 1

    is_round = True
    for move in complements:
        if move_dic.get(move,0) != move_dic.get(complements[move],0):
            is_round = False

    return is_round

def selfDividingNumbers(self, left, right):
  """
  :type left: int
  :type right: int
  :rtype: List[int]
  """
  list_of_self_div = []
  for number in range(left, right + 1):
      str_number = str(number)
      if "0" not in str_number:
          is_self_div = True
          for digit in str_number:
              if number % int(digit) != 0:
                  is_self_div = False

          if is_self_div:
              list_of_self_div.append(number)

  return list_of_self_div


#18-1-18
# Swap values SQL
UPDATE salary SET sex =
        CASE WHEN sex = 'm'
        THEN 'f'
        ELSE 'm'
        END
# sum of pairs to be max. O(n log n)
def arrayPairSum(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      sorted_array = sorted(nums)
      pairs_sum = 0
      for i in range(0,len(sorted_array) - 1,2):
          pairs_sum += sorted_array[i]

      return pairs_sum
 
#19-1-18
def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    bin_rep = bin(num)
    comp_bin_rep = str(bin_rep[:2]) + ''.join([str(1 - int(n)) for n in bin_rep[2:]])
    comp_num = int(comp_bin_rep,2)
    return comp_num
