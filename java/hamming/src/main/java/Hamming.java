public class Hamming {
    private String leftStrand;
    private String rightStrand;
    private int hammmingDistance;
    public Hamming(String leftStrand, String rightStrand) {
        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
        if (this.leftStrand.length() != this.rightStrand.length()) {
            if (this.leftStrand.length() == 0) {
                throw new IllegalArgumentException("left strand must not be empty.");
            } else if (this.rightStrand.length() == 0) {
                throw new IllegalArgumentException("right strand must not be empty.");
            } else {
                throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
            }
        }
        this.hammmingDistance = getHammingDistance();
    }

    public int getHammingDistance() {
        int hammmingDistance = 0;
        
        for (int i = 0; i < leftStrand.length(); i++){
            if (leftStrand.charAt(i) != rightStrand.charAt(i)) {
                hammmingDistance += 1;
            }
        }
        return hammmingDistance;
    }
}
