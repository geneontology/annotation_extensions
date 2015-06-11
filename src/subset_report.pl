#!/usr/bin/env perl -w
use strict;

# Quick script for rough report on names and namespaces


my $obo = &slurp($ARGV[0]);

my @rel = split /\n\[Typedef\]\n/, $obo;
my $header = (shift @rel);

for (@rel) {
  my @subsets = ();
  my $id = '';
  my $name = '';
  my $xref = '';
  my @tag_value = split /\n/, $_;
  for my $tv (@tag_value) {
    my @tv = split /\: /, $tv;
    $id = $tv[1] if ($tv[0] eq 'id');
    $name = $tv[1] if ($tv[0] eq 'name');
    $xref = $tv[1] if (($tv[0] eq 'xref')&&($tv[1] =~ m/(RO|GOREL):\d{7}/)); # Assumes only 1 match!
    push @subsets, $tv[1] if ($tv[0] eq 'subset');
  }
  print "$id\t$name\t$xref\t";
  my @sorted_subsets = sort @subsets;
  while (@sorted_subsets) {
    print shift @sorted_subsets;
    print ", " if (@sorted_subsets >= 1);
  }
    print "\n";
}



sub slurp
{
	local $/;
	open SLURP, $_[0] or die "Can't open target $_[0]\n";
	my $obo = <SLURP>;
	close SLURP or die "cannot close target $_[0]\n";
	warn "Warning - this OBO file has multiple newlines at the end. This will crash Peeves!", if ($obo =~ m/\n\n\n\z/);
	return $obo;
}

