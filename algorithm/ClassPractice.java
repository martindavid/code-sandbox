
public class ClassPractice{

  public static void main(String[] args){
    Movies movie = new Movies();
    movie.printMovies();
    System.out.println();
    movie.printMovies(1, "Star Wars");
    System.out.println();
    movie.printMovies("Test, Test2, Test3");
    System.out.println("Is StarWars favorite ? " + movie.isAFavorite("StarWars"));
  }
}
