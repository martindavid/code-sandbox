public class JavaArray {

  public static void main(String[] args) {
    int[][] tTable = new int[10][];
    for (int i = 0; i < 10; ++i) tTable[i] = new int[10];
    for (int i = 0; i < tTable.length; ++i) {
      for (int j = 0; j < tTable[i].length; ++j) {
        tTable[i][j] = (i + 1)*(j + 1);
      }
    }

    for (int[] row : tTable) {
      for (int n : row) System.out.printf("%4d", n);
      System.out.println();
    }
  }
}
