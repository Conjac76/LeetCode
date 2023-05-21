class Solution {
    public boolean isAnagram(String s, String t) {
       int[] frequency = new int[26];
       for(int i = 0; i < frequency.length; i++) {
           frequency[i] = 0;
       }
       if(s.equals(t)) {
           return true;
       } else if(s.length() == t.length()) {
            for(int i = 0; i < s.length(); i++) {
                char temp = s.charAt(i);
                int pos = temp - 'a';
                frequency[pos] += 1;
                //System.out.print(frequency[pos]);
                char temp2 = t.charAt(i);
                int pos2 = temp2 - 'a';
                frequency[pos2] -= 1;
                //System.out.print(frequency[pos2]);
            }

            for(int j = 0; j < frequency.length; j++) {
                System.out.print(frequency[j]);
            }

            for(int k = 0; k < frequency.length; k++) {
                if(frequency[k] != 0) {
                    return false;
                }
            }
            return true;
        } else {
            return false;
        }
    }
}