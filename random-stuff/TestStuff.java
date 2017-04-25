import java.net.URI;
import java.net.URISyntaxException;
import java.util.Arrays;

public class TestStuff {

  public static void main(String[] args) {
    String[] arr = {"9D", "5H", "6D", "4H", "JH"};
    String[] arr2 = {"web", "html", "javascript"};
    String[] arr3 = {"web", "javascript"};
    String[] arr4 = {"javascript", "html"};
    String[] arr5 = { "web", "html", "github" };
    String[] test = {"web","github"};

    // System.out.println(isValid(arr2, test));
    // System.out.println(isValid(arr3, test));
    // System.out.println(isValid(arr4, test));
    // System.out.println(isValid(arr5, test));

    try {
      URI uri = new URI("");
      System.out.println(uri.getScheme());
      System.out.println(uri.isAbsolute());
    } catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    
  }

  public static Boolean isValid(String[] arr, String[] test) {
    return Arrays.asList(arr).containsAll(Arrays.asList(test));
  }
}
