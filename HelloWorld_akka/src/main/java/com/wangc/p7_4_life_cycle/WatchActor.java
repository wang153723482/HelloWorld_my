package com.wangc.p7_4_life_cycle;

import akka.actor.ActorRef;
import akka.actor.Terminated;
import akka.actor.UntypedActor;

/**
 * Created by wangchao on 2017/2/15.
 * Description: 监听
 */
public class WatchActor extends UntypedActor {

    public WatchActor(ActorRef actorRef) {
        getContext().watch(actorRef); //构造监听的时候，添加一个被监听actor
    }

    @Override
    public void onReceive(Object message) throws Throwable {
        if (message instanceof Terminated) {
            System.out.println(((Terminated) message).getActor().path());
            getContext().system().shutdown();//关闭整个actorSystem
        } else
            unhandled(message);
    }
}
