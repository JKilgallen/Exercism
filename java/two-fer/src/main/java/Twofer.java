public class Twofer {

    private String name;
    public String twofer(String name) {
        this.name = name == null ? "you" : name;
        return "One for " + this.name + ", one for me.";
    }

}
