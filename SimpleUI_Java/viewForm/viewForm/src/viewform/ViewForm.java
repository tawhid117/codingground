/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package viewform;

import au.com.bytecode.opencsv.CSVReader;
import java.io.FileReader;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Paint;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.scene.text.TextAlignment;
import javafx.stage.Stage;

/**
 *
 * @author Tawhid
 */
public class ViewForm extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("JFX WelCome");
        
//        boolean sobThikThak = false;
        
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(15);
        grid.setPadding(new Insets(25,25,25,25));
        
        Text label_heading = new Text("View Form");
        label_heading.setFont(Font.font("Comic Sans MS", FontWeight.EXTRA_BOLD, 25));
        label_heading.setFill(Paint.valueOf("red"));
        label_heading.setTextAlignment(TextAlignment.CENTER);
        grid.add(label_heading, 2, 0);
        
        Label label_user = new Label("User: ");
        label_user.setAlignment(Pos.TOP_LEFT);
        grid.add(label_user, 0, 0+2, 2, 1);
        TextField text_user = new TextField("");
        text_user.setAlignment(Pos.TOP_LEFT);
        grid.add(text_user, 2, 0+2);
 
        Label label_pass = new Label("Pass: ");
        label_pass.setAlignment(Pos.TOP_LEFT);
        grid.add(label_pass, 0, 1+2, 2, 1);
        PasswordField text_pass = new PasswordField();
        text_pass.setAlignment(Pos.TOP_LEFT);
        grid.add(text_pass, 2, 1+2);
        
        Button btn_show_data = new Button("Show Data");
        grid.add(btn_show_data, 5, 0+2);
        
        Label label_user2 = new Label("Username: ");
        Label label_user2_data = new Label(" ----- ");
        grid.add(label_user2, 0, 3+2, 2, 1); grid.add(label_user2_data, 2, 3+2);
        
        Label label_first_name = new Label("First Name: ");
        Label label_first_name_data = new Label(" ----- ");
        grid.add(label_first_name, 0, 4+2, 2, 1); grid.add(label_first_name_data, 2, 4+2);
        
        Label label_last_name = new Label("Last Name: ");
        Label label_last_name_data = new Label(" ----- ");
        grid.add(label_last_name, 0, 5+2, 2, 1); grid.add(label_last_name_data, 2, 5+2);
        
        Label label_address = new Label("Address: ");
        Label label_address_data = new Label(" ----- ");
        grid.add(label_address, 0, 6+2, 2, 1); grid.add(label_address_data, 2, 6+2);

        Label label_phone = new Label("Phone: ");
        Label label_phone_data = new Label(" ----- ");
        grid.add(label_phone, 0, 7+2, 2, 1); grid.add(label_phone_data, 2, 7+2);
        
        btn_show_data.setOnAction(new EventHandler<ActionEvent>() {
           @Override
           public void handle(ActionEvent e){
           
            String[] user_data = {};
                    
            user_data = fetch_data(text_user.getText(), text_pass.getText());   // username,first_name,last_name,address,phone,
               
           text_user.setText(""); text_pass.setText("");
           System.out.println(user_data[1]);
           label_user2_data.setText(user_data[0]);
           label_first_name_data.setText(user_data[1]);
           label_last_name_data.setText(user_data[2]);         
           label_address_data.setText(user_data[3]);
           label_phone_data.setText(user_data[4]);
             
           }
        } ) ;
        

        Scene scene = new Scene(grid, 800, 500); // window size
        scene.getStylesheets().add (ViewForm.class.getResource("viewFormCSS.css").toExternalForm());
        primaryStage.setScene(scene);
        
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
    
    
    public static String[] fetch_data(String text_username, String text_pass1){
        
        try
        {
            CSVReader pass_checker = new CSVReader(new FileReader("up.csv"));
            String[] line;
            while ((line = pass_checker.readNext()) != null) {
                System.out.println("user= " + line[0] + ", pass " + line[1] );
                if( line[0].equals(text_username) && line[1].equals(text_pass1) ){
                    try{
                        CSVReader data_reader = new CSVReader(new FileReader("userdata.csv"));
                        String[] line2;
                        while( (line2 = data_reader.readNext()) != null ){
                            if(line2[0].equals(text_username)){
                                return line2;
                            }
                        
                        }
                    }catch(Exception ee){System.out.println(ee);}
                }
            }
        } 
        catch (Exception e) {
              System.out.println(e);
        }
    String[] not_found = {"INCORRECT CREDENTIALS", "-", "-", "-", "-"};    
    return not_found ;
    }
    
}
