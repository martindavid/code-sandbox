public class FindFixPoint {

  public static void main(String[] args) {
    int[] arr = {-10,-5,0,3,7};

    System.out.println(search(arr, 0, arr.length - 1));

  }

  public static int IsFixedPointExists(int[] arr){
    for (int i = 0; i < arr.length; i++){
      if (arr[i] == i){
        return i;
      }
    }
    return -1;
  }

  // perform modified binary search
	public static int search(int[] A, int start, int end) {
		if (start <= end) {
			int mid = (start + end) / 2;
			if (mid == A[mid]) // check for magic index.
				return mid;
			if (mid > A[mid]) { // If mid>A[mid] means fixed point might be on
								// the right half of the array
				return search(A, mid + 1, end);
			} else {// If mid<A[mid] means fixed point might be on
				// the left half of the array
				return search(A, start, mid - 1);
			}
		}
		return -1;
	}

}
