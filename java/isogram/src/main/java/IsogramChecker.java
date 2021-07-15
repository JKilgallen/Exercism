class IsogramChecker {

    static final char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
    boolean isIsogram(String phrase) {
        for (int i = 0; i < 26; i++) {
            final char character = alphabet[i];
            if (phrase.toLowerCase().chars().filter(ch -> ch == character).count() > 1) {
                return false;
            }
        }
        return true;

    }

}
