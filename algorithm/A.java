public class A {
  private int y = 2;
  public int x = 1;
  public int mob(int y) { return x + y; }
  public static void main(String[] args){
    A a = new A();
    System.out.println(a.mob(3));
  }
}
