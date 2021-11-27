static変数（クラス変数）
クラス定義の直下で宣言する変数。
変数を宣言する時、static修飾子を指定することでstatic変数として扱われる。
インスタンス変数は、各オブジェクト毎に値を保持していたが、
static変数は、1箇所にまとめられて値を保持する（全てのオブジェクトに対して同じ値が使用される）。

インスタンス変数がインスタンス毎の変数であり、static変数（クラス変数）はクラス毎の変数となります。
class Sample {
  int number = 99; // インスタンス変数
  static String color = "黄"; // static変数（クラス変数）

  // static変数（クラス変数）に値をセットするメソッド
  public void setColor(String value) {
    color = value;
  }
}


class Main {
    public static void main(String args[]) {
        Sample sample1 = new Sample();

        sample1.number = 10;
        System.out.println(sample1.number); // 10
        sample1.setColor("赤");
        System.out.println(Sample.color); // 赤

        Sample sample2 = new Sample();
        // インスタンス変数であるnumberは、オブジェクト毎に保持しているものなので、初期値の99が入っている。
        System.out.println(sample2.number); // 99

        // static変数（クラス変数)のcolorは共通の値を共有するため、
    // デフォルトの「黄」はsample1.setColorのタイミングで赤がセットされた。
    // だからここでstatic変数（クラス変数）にアクセスすると赤と出力される。
    System.out.println(Sample.color); // 赤
}


}
