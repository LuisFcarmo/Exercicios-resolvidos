package l2.q1;

public class teste {
    public static void main(String[] args) {
        empresa CasasBahia = new empresa("casa bahia", "23323232");
        CasasBahia.CriarDepartamento(0, "patio");
        for (int i = 0; i < 10; i++) {
            funcionario x = new funcionario("Luisinho", 100.0, "10/10/2002");
            CasasBahia.GetDepartamento(0).AdicionarColaborador(x);
        }

        CasasBahia.GetDepartamento(0).ListarColaboradores(3);
        CasasBahia.GetDepartamento(0).aumentar();
        CasasBahia.GetDepartamento(0).ListarColaboradores(3);
    }
}
