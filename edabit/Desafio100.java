import java.util.ArrayList;

public class Desafio100 {
 
    public static void main(String[] args) {

        ArrayList <Integer> list = new ArrayList<>();
        list.add(100);
        list.add(170);
        boolean verify = false;
        for(Integer number: list) {
            if(Integer.toString(number).contains("7")){
                return("Boom!");
            }
        }
        return("there is no 7 in the array");

    }
}
