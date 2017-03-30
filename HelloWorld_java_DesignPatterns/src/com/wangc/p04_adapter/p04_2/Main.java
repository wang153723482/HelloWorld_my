package com.wangc.p04_adapter.p04_2;

import javax.swing.plaf.basic.BasicComboPopup;

/**
 * @author: wangchao
 * Date: 2016/3/5 16:14
 * Description:
 */
public class Main {
    
    public class T2{
        public int age = 12;
    }
    
    public static void main(String[] args){
        
        EventAdapter eventAdapter = new EventMyImp();
        eventAdapter.move();
        eventAdapter.click();

        
        

    }
}

class EventMyImp extends EventAdapter{
    @Override
    public void move() {
        super.move();
        System.out.println("you are moved.");
        Main m = new Main();
        Main.T2 t = m.new T2();
        System.out.println( t.age );
        
    }
}
