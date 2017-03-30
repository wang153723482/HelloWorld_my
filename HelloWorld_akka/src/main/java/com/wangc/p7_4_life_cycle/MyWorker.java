package com.wangc.p7_4_life_cycle;

import akka.actor.UntypedActor;

/**
 * Created by wangchao on 2017/2/15.
 */
public class MyWorker extends UntypedActor {

    public static enum Msg {
        WORKING, DONE, CLOSE;
    }

    @Override
    public void preStart() throws Exception {
        System.out.println("MyWorker is starting.");
    }

    @Override
    public void postStop() throws Exception {
        System.out.println("MyWorker is stopping.");
    }

    @Override
    public void onReceive(Object message) throws Throwable {
        if (message == Msg.WORKING) {
            System.out.println("i am working.");
        } else if (message == Msg.DONE) {
            System.out.println("stopping working.");
        } else if (message == Msg.CLOSE) {
            System.out.println("i will shutdown.");
            getSender().tell(Msg.CLOSE, getSelf());
            getContext().stop(getSelf());
        } else {
            unhandled(message);
        }
    }
}
