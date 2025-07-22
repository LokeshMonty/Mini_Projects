import java.awt.*;
import java.awt.event.*;
import java.awt.Graphics;
class DemoBill extends Frame implements ActionListener
{
			Label l1,l2,l3,l4,l5;
			TextField t1,t2,t4,t5;
			TextArea t3;
			Button b1,b2;

			DemoBill()
			{
				setLayout(null);

l1=new Label("Electricity Bill Calculator");
l2=new Label("Customer Name");
l3=new Label("Customer ID");
l4=new Label(" Enter Units ");
l5=new Label(" Final bill ");

b1 = new Button("Calculate bill");
b2 = new Button("Print");

			t1=new TextField();
			t2=new TextField();
			t3=new TextArea();
			t4=new TextField();
			t5=new TextField();

			add(l1);
			add(t3);
			add(l4);
			add(t1);
			add(t2);
			add(b1);
			add(l5);
			add(b2);
			add(l2);
			add(l3);
			add(t4);
			add(t5);
	
			l1.setBounds(250,60,200,50);
			l2.setBounds(50,120,100,30);
			l3.setBounds(50,180,100,30);
			l4.setBounds(280,120,100,30);
			l5.setBounds(280,180,100,30);
	
			t1.setBounds(380,120,100,30);
			t2.setBounds(380,180,100,30);
			t3.setBounds(150,290,300,200);
			t4.setBounds(150,120,100,30);
			t5.setBounds(150,180,100,30);
		
			b1.setBounds(250,240,100,30);
			b2.setBounds(250,510,100,30);
	
				b1.addActionListener(this);
			}
			public void actionPerformed(ActionEvent ae)
			{
				int a=Integer.parseInt(t1.getText());
		
				long c=Long.parseLong(t5.getText()); 
				String d=String.valueOf(t4.getText());
				double amt = 0; 
  
				if(ae.getSource()==b1)
				{     
        	  		 if(a <= 100) 
					{
            				amt = 8.80 * a;
        			}
        			else if (a <= 200) 	
					{
            				amt = 8.80 * 100 + (a - 100) * 9.0;
        			}
        			else 
					{
            				amt = 8.80 * 100 + 9.0 * 100 + (a - 200) * 9.20;
					}
        		}
        		
			t2.setText(amt+" ");
		
t3.setText(" Customer name = " +d+ " \n\n Customer ID = " +c+ " \n\n Total units = " +a+ " \n\n Total payable amount = Rs " +amt );
		}

			public static void main(String args[])
			{
			DemoBill b=new DemoBill();
			b.setVisible(true);
			b.setSize(600,600);
			}

}
