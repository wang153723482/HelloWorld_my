package com.wangc.p7_2_hello_world;

import akka.actor.UntypedActor;
import com.wangc.Msg;


/**
 * Created by wangchao on 2017/1/22.
 * Description:一个 actor ，如果接收到的消息是 hello ，则打印语句，并返回给发送者一个消息 over ;
 *              如果接收的消息不是 hello ，则返回给发送者一个消息 unmsg 。也可以不返回。
 */
public class Greeter extends UntypedActor {

    public void onReceive(Object message) throws Throwable {
        if (Msg.HELLO.equals(message)) {//收到greet的消息时
            System.out.println("Greeter====Hello World! i got=== " + message);
            //getSender() 获取消息的发送者，调用tell()进行消息回复
            getSender().tell(Msg.OVER, getSelf());
            getSender().tell("o1", getSelf());
            getSender().tell("o2", getSelf());
            getSender().tell("o3", getSelf());
            getContext().stop(getSelf());
        } else {
            unhandled(message);
            System.out.println("Greeter===unhandled===" + message);
            getSender().tell(Msg.UNMSG, getSelf());
        }

    }
}
