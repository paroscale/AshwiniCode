//Starting the serf agent
package main

import (
        "fmt"
        "os"
        "strconv"
        "crypto/rand"
        "math/big"
        "time"
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
					fmt.Println(event.(serf.MemberEvent).Members, "joined")
				case "member-update":
					fmt.Println(event.(serf.MemberEvent))
				default:
					fmt.Println("Not occurring : ", event)
			}
		}
	}
}

func keygeneration() string {
        // generate key
        const (
                keyList string = "abcdefghijklmnopqrstuvwxyzABCDEFHFGHIJKLMNOPQRSTUVWXYZ1234567890"
            )
        size := "32"
        strLen, _ := strconv.Atoi(size)
        var stringGen string 
        for key := 1; key <= strLen; key++ {
                res, _ := rand.Int(rand.Reader, big.NewInt(64))
                keyGen := keyList[res.Int64()]
                stringGen = fmt.Sprintf("%c", keyGen)
		fmt.Printf((stringGen))
            }
        fmt.Printf((stringGen))  
        return string(stringGen)
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

        if join_addr == "0"{
                var keyvalue string
                keyvalue = keygeneration()
                fmt.Println("key is:" ,keyvalue)
                a := serf.KeyManager{}
                b , _:= a.InstallKey(keyvalue)
                fmt.Println("b value is:", b)
                time.Sleep(10*time.Second)
              
        }else{
                fmt.Println("no key found")
        }
        for{
                       
        }
}
