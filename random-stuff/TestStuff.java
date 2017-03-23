public class TestStuff {

  public static void main(String[] args) {
    String[] arr = {"9D", "5H", "6D", "4H", "JH"};
    System.out.println(arr[4].charAt(0));
    System.out.println(arr[4].substring(0,1));
    System.out.println(Character.digit("A".charAt(0), 10));
  }
}
