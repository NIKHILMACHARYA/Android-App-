
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;
import android.widget.ArrayAdapter;
import java.util.ArrayList;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {
    private ListView listView;
    private ArrayList<String> itemList;
    private ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize ListView
        listView = findViewById(R.id.listView);

        // Create sample data
        itemList = new ArrayList<>(Arrays.asList(
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5"
        ));

        // Create and set adapter
        adapter = new ArrayAdapter<>(
            this,
            android.R.layout.simple_list_item_1,
            itemList
        );
        listView.setAdapter(adapter);
    }
}
