package com.wangc.p7_2_hello_world;

import akka.actor.ActorRef;
import akka.actor.Props;
import akka.actor.UntypedActor;
import com.wangc.Msg;

/**
 * Created by wangchao on 2017/1/22.
 * Description: 另外一个actor
 */
public class HelloWorld extends UntypedActor{
    ActorRef greeter;
    
//    @Override
//    public void preStart() throws Exception {
//        greeter = getContext().actorOf(Props.create(Greeter.class),"greeterx2");
//        System.out.println("Greeter Actor Path: "+greeter.path());
//        greeter.tell("greet",getSelf());
//    }

    public void onReceive(Object message) throws Throwable {
        if(Msg.OVER.equals(message) ){
//            greeter.tell("hello two",getSelf());
            System.out.println("HelloWorld===i got==="+message);
//            getSender().tell("hello2",getSelf());
//            getContext().stop(getSelf());//将自己停止，对方无法发信过来
        }else{
            unhandled(message);
            System.out.println("HelloWorld===unhandled==="+message);
        }
    }
}
