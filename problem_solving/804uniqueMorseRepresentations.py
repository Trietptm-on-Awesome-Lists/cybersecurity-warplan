  def uniqueMorseRepresentations(self, words):
      """
      :type words: List[str]
      :rtype: int
      """
      m_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
      len_of_m_table = len(m_table)
      alph_table = [chr(x) for x in range(ord('a'),ord('a') + len_of_m_table)]
      morse_dict = {alph_table[x]:m_table[x] for x in range(len_of_m_table)}

      uniq_elems = set()
      for each_word in words:
          morse_str = "".join([morse_dict[each_word[x]] for x in range(len(each_word))])
          uniq_elems.add(morse_str)

      return (len(uniq_elems))
