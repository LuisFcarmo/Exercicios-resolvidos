package l2.q1;

public class funcionario {
    private String name;
    private double salario;
    private String data;

    public funcionario() {
    };

    public funcionario(String name, double salario, String data) {
        super();
        this.name = name;
        this.salario = salario;
        this.data = data;
    }

    public String GetName() {
        return this.name;
    }

    public double GetSalario() {
        return this.salario;
    }

    public String GetData() {
        return this.data;
    }

    public void SetSalario(Double salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        return String.format("{ name: %s \ndata: %s \nsalario: %.2f }\n", this.name, this.data, this.salario);

    }
}