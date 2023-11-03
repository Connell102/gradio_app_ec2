import gradio

def hello(inp):
  return "Hello {}!".format(inp)

io = gradio.Interface(fn=hello, inputs='text', outputs='text', title='Hello World', 
    description='The simplest Hosted interface.', server_name="0.0.0.0")  
io.launch()
