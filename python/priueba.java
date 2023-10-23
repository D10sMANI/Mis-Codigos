 import java.awt.geom.Point2D;
   import java.util.Random;
   public class MyClass {
       public static void main(String args[]) {
         int n=10000000;
         int insideCircle = 0;
         for(int i = 1; i <= n; i++){
             Random rand = new Random();
             double x = rand.nextDouble(2) -1d;
             double y = rand.nextDouble(2) -1d;
             if(isInsideCircle(x,y)){
                 insideCircle++; 
             }
         }
         System.out.println("pi value: " + 4*(double)insideCircle/(double)n);
       }
       
       public static boolean isInsideCircle( 
           double x1, 
           double y1) {
           return Point2D.distance(x1, y1, 0, 0) <= 1;
       }
   }