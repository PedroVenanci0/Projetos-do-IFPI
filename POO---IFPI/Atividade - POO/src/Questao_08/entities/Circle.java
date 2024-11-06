package Questao_08.entities;

public class Circle {

    // atributos
    private Double raio;

    public Circle(){
    }

    public Circle(Double raio){
        this.raio = raio;
    }

    public Double calcularArea(){
        return Math.PI * raio*raio;
    }

    public Double calcularPerimetro(){
        return  (2 * Math.PI * raio);
    }
}
