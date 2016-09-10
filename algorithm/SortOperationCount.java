public class SortOperationCount {

  public static void main(String[] args){
    int[] testCase = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    //insertionSort(testCase);
    selectionSort(testCase);
  }



  public static void insertionSort(int[] array) {
        int firstValue;                // first value in  array
        int scan;                    // scan array through the array
        int moves = 0;            //  number of moves
        int compares = 0;      //  number of comparisons
        int total;                // total number of operations

        for (int index = 1; index < array.length; index++) {

            firstValue = array[index];

            moves++;// count as a move

            scan = index;

            while (scan> 0 && array[scan - 1] > firstValue) {

                array[scan] = array[scan - 1];

                compares++; // count as a compare
                moves++;     // count as a move
                scan--;
            } compares++; // count as a comparison

            array[scan] = firstValue;
            moves++;       // count as a move
    }

        total = compares + moves;

        // Display the number of assignments
        System.out.println("# of comparisons: "
                + compares);
        System.out.println("# of moves: " + moves);
        System.out.println("Total number of operations: " +  total);

    }

    public static void selectionSort(int[] array) {

          int start;              //  starting point of array
          int index;              // index of an array element
          int minIndex;              // element with smallest value
          int minValue;                //  smallest value in array
          int swaps = 0;             // swaps
          int comparisons = 0;       //  comparisons
          int total;                  // The total number of operations

          for (start = 0; start < (array.length - 1); start++) {

              minIndex = start;
              minValue = array[start];
              swaps++; // count swap

              for (index = start + 1; index < array.length; index++){

                  if (array[index] < minValue) {

                     comparisons++; // count comparison
                      minValue = array[index];
                      swaps++; // count the swap
                      minIndex = index; // not sure if this should be counted as it is dealing with an index
                  }
              } comparisons++; // count comparison [b](not sure if this should be here)[/b]

              array[minIndex] = array[start];
              swaps++; // count the swap
              array[start] = minValue;
              swaps++; // count the swap
          }

          total = comparisons + swaps;

          // Display the number of assignments
          System.out.println("# of comparisons: "
                  + comparisons);
          System.out.println("# of swaps: " + swaps);
          System.out.println("Total number of operations: " +  total);
      }
}
