# ProcyonCLS App Market

## Uploading Your Application

To upload your application to the ProcyonCLS App Market, follow these steps:

/!\ **Note**: Before uploading your application, make sure that it is working correctly and that it follows the guidelines provided in the ProcyonCLS documentation. Also it's first come first serve in terms of naming, so make sure your application name is unique.

1. **Fork the Repository**: Fork the `ProcyonCLS-AppMarket` repository to your GitHub account.
2. **Clone the Repository**: Clone the forked repository to your local machine.
   ```sh
   git clone https://github.com/yourusername/ProcyonCLS-AppMarket.git
   cd ProcyonCLS-AppMarket
   ```
3. **Add your Application**: Add your application to the `apps` directory.
    ```sh
    cp /path/to/your/app.py apps/
    ```
4. **Commit and Push**: Commit your changes and push them to your forked repository.
    ```sh
    git add apps/app.py
    git commit -m "Add MyApp - DeveloperName - Version - Description"
    git push origin main
    ```
5. **Create a Pull Request**: Create a pull request from your forked repository to the main repository.

Once your pull request is approved, your application will be added to the ProcyonCLS App Market.

### Conclusion

This document has provided an overview of how to develop applications for ProcyonCLS. For more information on developing applications for ProcyonCLS, refer to the sample.py file in the ProcyonCLS repository.
