package q2;

public class loteria {
    private int numero_premiado;
    private int tentativa;
    loteria() {
        numero_premiado = (int) (Math.random() * 10 )+ 1;
        this.tentativa = 0;
    }

    public int tentativas () {
        return this.tentativa;
    }

    public int chutar (int chute) {
        if (chute > numero_premiado) {
            return 1;
        }
        else if (chute < numero_premiado) {
            return 2;
        } 
        else {
            return 3;
        }
    }
}
