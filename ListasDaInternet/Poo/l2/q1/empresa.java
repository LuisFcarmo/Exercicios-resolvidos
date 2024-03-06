package l2.q1;

import java.util.ArrayList;
import java.util.List;

public class empresa {
    private String name;
    private String CNPJ;
    private List<departamento> departamentos = new ArrayList<departamento>();

    empresa(String name, String CNPJ) {
        super();
        this.name = name;
        this.CNPJ = CNPJ;
    }

    public String GetName() {
        return this.name;
    }

    public void ListarDepartamentos() {
        for (int i = 0; i < departamentos.size(); i++) {
            System.out.println(departamentos.get(i).GetName());
        }
    }

    public void CriarDepartamento(int id, String name) {
        departamentos.add(new departamento(id, CNPJ));
    }

    public void ListarFuncionariosDepartamento(int id, int quantidade) {
        departamentos.get(id).ListarColaboradores(quantidade);
    }

    public departamento GetDepartamento(int id) {
        return departamentos.get(id);
    }
}
