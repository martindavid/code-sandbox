public class Movies{
  // Print out my 5 favorites movies
  public void printMovies() {
    System.out.println("1. Star Wars");
    System.out.println("2. Star Trek");
    System.out.println("3. Lord of The Rings Trilogy");
    System.out.println("4. The Hobbit Trilogy");
    System.out.println("5. Marvels Movies");
  }

  // Print a name of movie with its rank
  // Accept rank and movie name as an input
  public void printMovies(int rank, String movieName){
    System.out.println(String.format("%d. %s", rank, movieName));
  }

  // Parse a string contain list of movies and print out the result in order
  public void printMovies(String listOfMovies) {
    String[] movies = listOfMovies.split(",");
    for (int i = 0; i < movies.length; i++) {
      System.out.println(String.format("%d. %s", i, movies[i].trim()));
    }
  }


  public boolean isAFavorite(String movieName){
    String movieList = "StarWars, StarTrek, LordOfTheRing, TheHobbit, WorldOfWarcraft";
    return movieList.contains(movieName);
  }
}
