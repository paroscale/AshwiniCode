//Starting the serf agent
package main

import (
        "fmt"
        "os"
        "strconv"
        "crypto/rand"
        "math/big"
        "io/ioutil"
	"time"
        "log"
        "github.com/hashicorp/serf/serf"
)

func EventHandlers(ch chan serf.Event) {
	for {
		select {
		case event := <-ch:
			switch event.String() {
				case "user-event: data":
					fmt.Println("User event occured")
					//fmt.Printf("%s\n", event.(serf.UserEvent).Payload)
				case "member-join":
					fmt.Println(event.(serf.MemberEvent).Members, "new agent joined")
				case "member-update":
					fmt.Println(event.(serf.MemberEvent))
				default:
					fmt.Println("Not occurring : ", event)
			}
		}
	}
}

const (
    keyList string = "abcdefghijklmnopqrstuvwxyzABCDEFHFGHIJKLMNOPQRSTUVWXYZ1234567890"
)

func ReadFile() string {
	data, err := ioutil.ReadFile("keyringFile")
	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}
	fmt.Printf("\nData: %s\n", data)
        return string(data)
}

func main() {
        //Get agent name and port from cmd line args
        port := os.Args[1]
        join_addr := os.Args[2]
        fmt.Printf("Port mentioned %v , addr to join mentioned %v \n", port, join_addr)

        //Create a serf agent
        cfg := serf.DefaultConfig()
        event_ch := make(chan serf.Event, 10)
        cfg.EventCh = event_ch
        cfg.NodeName = port
        //Make logger as dummy
        cfg.EventBuffer = 3 //Make as no of node
        cfg.MemberlistConfig.BindPort, _ = strconv.Atoi(port)
        obj, err := serf.Create(cfg)
        if err != nil {
                fmt.Println("Error with starting agent")
                os.Exit(1)
        } else {
                fmt.Println("Started agent sucessfully!")
        }
       
        go EventHandlers(event_ch)

        //Join a cluster
        if join_addr != "0" {
                ar := []string{join_addr}
                no, _ := obj.Join(ar, false)
                if no > 0 {
                        fmt.Println("Joined cluster sucessfully, no of nodes contacted sucessfully ", no)
                        no_of_nodes := obj.NumNodes()
                        fmt.Println("No of nodes in cluster ", no_of_nodes)
                } else {
                        fmt.Println("Unable to contact metioned node addrs")
                }
        } else {
                fmt.Println("No join addr issued")
        }
	for{
        size := "31"
	strLen, _ := strconv.Atoi(size)
	filename := "keyringFile"
	os.Create(filename)
        f, _ := os.OpenFile(filename, os.O_APPEND|os.O_WRONLY, 0777)
	for key := 1; key <= strLen; key++ {
		res, _ := rand.Int(rand.Reader, big.NewInt(64))
		keyGen := keyList[res.Int64()]
		stringGen := fmt.Sprintf("%c", keyGen)
		f.Write([]byte(stringGen))
	}
        var key string
        key = ReadFile()
        fmt.Println("key is:" ,key)
        a := serf.KeyManager{}
        b , err := a.InstallKey(key)
        if err != nil {
                fmt.Println("error is " , err)
        } else {
                fmt.Println("no error found")
        }
        fmt.Println("b value: " , b)
        time.Sleep(10*time.Second)
	}
        
}
