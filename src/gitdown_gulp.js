var gulp = require('gulp'),
    Gitdown = require('gitdown');

// TODO: edit to iterate of AE markdown files

gulp.task('gitdown', function () {
    return Gitdown
        .read('.gitdown/README.md')
        .write('README.md');
});

gulp.task('watch', function () {
    gulp.watch(['./.gitdown/*'], ['gitdown']);
});
