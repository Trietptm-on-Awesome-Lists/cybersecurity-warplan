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
