import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.io.IOException;  
import org.jsoup.Jsoup;
import org.jsoup.helper.Validate;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.*;



public class Crawler
{
  // private static final int MAX_PAGES_TO_SEARCH = 10;
  // private Set<String> pagesVisited = new HashSet<String>();
  // private List<String> pagesToVisit = new LinkedList<String>();


  // /**
  //  * Our main launching point for the Spider's functionality. Internally it creates spider legs
  //  * that make an HTTP request and parse the response (the web page).
  //  * 
  //  * @param url
  //  *            - The starting point of the spider
  //  * @param searchWord
  //  *            - The word or string that you are searching for
  //  */
  // public void search(String url, String searchWord)
  // {
  //     while(this.pagesVisited.size() < MAX_PAGES_TO_SEARCH)
  //     {
  //         String currentUrl;
  //         SpiderLeg leg = new SpiderLeg();
  //         if(this.pagesToVisit.isEmpty())
  //         {
  //             currentUrl = url;
  //             this.pagesVisited.add(url);
  //         }
  //         else
  //         {
  //             currentUrl = this.nextUrl();
  //         }
  //         leg.crawl(currentUrl); // Lots of stuff happening here. Look at the crawl method in
  //                                // SpiderLeg
  //         boolean success = leg.searchForWord(searchWord);
  //         if(success)
  //         {
  //             System.out.println(String.format("**Success** Word %s found at %s", searchWord, currentUrl));
  //             break;
  //         }
  //         this.pagesToVisit.addAll(leg.getLinks());
  //     }
  //     System.out.println("\n**Done** Visited " + this.pagesVisited.size() + " web page(s)");
  // }


  // /**
  //  * Returns the next URL to visit (in the order that they were found). We also do a check to make
  //  * sure this method doesn't return a URL that has already been visited.
  //  * 
  //  * @return
  //  */
  // private String nextUrl()
  // {
  //     String nextUrl;
  //     do
  //     {
  //         nextUrl = this.pagesToVisit.remove(0);
  //     } while(this.pagesVisited.contains(nextUrl));
  //     this.pagesVisited.add(nextUrl);
  //     return nextUrl;
  // }
      public static void Main(String[] args)
    {
        String url = "wwww.google.com";
        System.out.println("Fetching %s...");
        Document doc = new Document();
        Elements links = doc.select("a[href]");
          }

}

// class SpiderTest
// {
//     /**
//      * This is our test. It creates a spider (which creates spider legs) and crawls the web.
//      * 
//      * @param args
//      *            - not used
//      */
//     public static void main(String[] args)
//     {
//         Spider spider = new Spider();
//         spider.search("http://arstechnica.com/", "computer");
//     }
// }