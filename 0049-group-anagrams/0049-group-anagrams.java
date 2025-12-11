class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] ch = s.toCharArray();
            Arrays.sort(ch);
            String key = new String(ch); // use sorted string as the key
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        List<List<String>> fini = new ArrayList<>(map.values());
        return fini;
    }
}
