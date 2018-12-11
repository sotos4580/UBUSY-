package com.example.evansotos.firebasepybase;

import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        FirebaseFirestore db = FirebaseFirestore.getInstance();
        final TextView header = (TextView) this.findViewById(R.id.header);
        final TextView minutes = (TextView) this.findViewById(R.id.minuteTime);
        final Button refreshBtn = (Button) this.findViewById(R.id.refreshContent);
        final ProgressBar busyness = (ProgressBar) this.findViewById(R.id.progress_bar);
        int currTime = (int)System.currentTimeMillis();
        long mins = TimeUnit.MILLISECONDS.toMinutes(currTime);

        // Create a new user with a first and last name
        Map<String, Object> storeObj = new HashMap<>();
        storeObj.put("Date", "12/04/18");
        storeObj.put("Time", "5:32");
        storeObj.put("People", 755);

// Add a new document with a generated ID
        db.collection("proProcessed")
                .add(storeObj)
                .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
                    @Override
                    public void onSuccess(DocumentReference documentReference) {
                        Log.d("SUCCESS", "DocumentSnapshot added with ID: " + documentReference.getId());
                        header.setText(documentReference.getId());
                    }
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Log.w("WARN", "Error adding document", e);
                    }
                });


        refreshBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                minutes.setText("Minute Update");
                busyness.setProgress(96);
            }
        });

    }
}
