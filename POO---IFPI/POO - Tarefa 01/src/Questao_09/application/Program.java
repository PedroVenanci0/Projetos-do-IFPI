package Questao_09.application;
import Questao_09.entities.Financeiro;

public class Program {
    public static void main(String[] args){
        Financeiro financeiro = new Financeiro(4.0, 5.0);
        System.out.println("Seu Saldo: " + financeiro.calcularSaldo());
    }
}
