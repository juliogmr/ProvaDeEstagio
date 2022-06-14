public class Questao4 {

	public static void main(String[] args) {
		
		double sp = 67836.43;//SP
		double rj = 36678.66;//RJ
		double mg = 29229.88;//MG
		double es = 27165.48;//ES
		double outros = 19849.53;
		
		double total = sp + rj + mg + es + outros;
		
		System.out.println("O percentual de representação que cada estado teve dentro do valor "
				+ "total mensal da distribuidora foram de: ");
		System.out.printf("SP: %.2f", sp/total*100);
		System.out.println("%");
		System.out.printf("RJ: %.2f", rj/total*100);
		System.out.println("%");
		System.out.printf("MG: %.2f", mg/total*100);
		System.out.println("%");
		System.out.printf("ES: %.2f", es/total*100);
		System.out.println("%");
		System.out.printf("Outros estados: %.2f", outros/total*100);
		System.out.println("%");
	}
}
