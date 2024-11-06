package Questao_09.entities;

public class Financeiro {

    private Double valorCredito;
    private Double valorDebito;

    public Financeiro(Double valorCredito, Double valorDebito){
        this.valorDebito = valorDebito;
        this.valorCredito = valorCredito;
    }

    public Double calcularSaldo(){
        return (valorCredito - valorDebito);
    }

}
