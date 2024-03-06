package l2.q1;

import java.util.ArrayList;
import java.util.List;

public class departamento {
    private List<funcionario> funcionarios;
    private int id;
    private String name;

    departamento(int id, String name) {
        super();
        this.id = id;
        this.name = name;
        funcionarios = new ArrayList<funcionario>();
    }

    public boolean AdicionarColaborador(funcionario x) {
        if (funcionarios.size() <= 100) {
            funcionarios.add(x);
            return true;
        }
        return false;
    }

    public void ListarColaboradores(int quantidade) {
        for (int i = 0; i < quantidade; i++) {
            System.out.println(funcionarios.get(i));
        }
    }

    public void aumentar() {
        for (funcionario x : funcionarios) {
            double salarioAtual = x.GetSalario();
            double aumento = salarioAtual * 0.1;
            double novoSalario = salarioAtual + aumento;
            x.SetSalario(novoSalario);
        }
    }

    public int GetId() {
        return this.id;
    }

    public String GetName() {
        return this.name;
    }

    @Override
    public String toString() {
        return "Name" + this.name;
    }
}