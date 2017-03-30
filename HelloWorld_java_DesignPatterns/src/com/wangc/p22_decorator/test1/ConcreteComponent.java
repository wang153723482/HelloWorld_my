package com.wangc.p22_decorator.test1;

/**
 * Created by wangchao on 2016/11/14.
 * 被装饰者
 */
public class ConcreteComponent extends Component {
    @Override
    public double calcPrize(String user) {
        return 800;//默认有800的基本工资
    }
}
