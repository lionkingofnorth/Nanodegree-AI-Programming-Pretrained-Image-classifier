

def test():
    with open('imagenet1000_clsid_to_human.txt') as f:
        output=eval(f.read())
    for _,v in output.items():
        print("v: {} \n ".format(v.lower().strip()))
    
    print("\n output {} \n type: {}".format(output,type(output)))

def main():
    test()

if __name__ == "__main__":
    main()