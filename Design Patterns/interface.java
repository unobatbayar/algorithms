interface Car {
    void start();
    void stop();
}

class Tesla implements Car {
    public void start() {
        System.out.println("Tesla is starting.");
    }

    public void stop() {
        System.out.println("Tesla is stopping.");
    }
}
