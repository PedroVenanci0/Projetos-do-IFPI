package Questao_07.application;
import Questao_07.entities.Rectangle;

public class Program {

    public static void main(String[] args){

        // creating instance
        Rectangle rectangle = new Rectangle();

        // set values with method
        rectangle.setValues(10.0, 4.0);

        // show values
        System.out.println("Area: " + rectangle.calculateArea());
        System.out.println("Perimeter: " + rectangle.calculatePerimeter());
    }

}
