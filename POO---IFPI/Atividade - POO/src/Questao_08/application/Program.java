package Questao_08.application;
import Questao_08.entities.Circle;

public class Program {
    public static void main(String[] args){

        Circle circle = new Circle(2.23);

        System.out.println("Area: " + circle.calcularArea());
        System.out.println("Perimetro: " + circle.calcularPerimetro());
    }
}
