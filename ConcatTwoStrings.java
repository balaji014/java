public  class ConcatTwoStrings {
    public static String concat(String str1, String str2) {
        return str1 + str2;
    }

    public static void main(String[] args) {
        String firstString = "Hello, ";
        String secondString = "World!";
        String result = concat(firstString, secondString);
        System.out.println(result); // Output: Hello, World!
    }
}
