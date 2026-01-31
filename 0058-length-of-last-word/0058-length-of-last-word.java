class Solution {
    public int lengthOfLastWord(String s) {
        int length = s.length();
        int count = 0;

        // Start from the end of the string
        int i = length - 1;
        
        // Skip any trailing spaces
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }
        
        // Count the characters of the last word
        while (i >= 0 && s.charAt(i) != ' ') {
            count++;
            i--;
        }
        
        return count;
    }
}
